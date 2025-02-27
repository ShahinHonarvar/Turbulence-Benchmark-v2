def palindromes_between_indices(s):
    letters = [char for char in s[7:9] if char.isalpha()]
    letters = [char.lower() for char in letters]
    arrangements = []
    for i in range(len(letters[0]) + 1):
        for j in range(len(letters[1]) + 1):
            arrangements.append(letters[0][:i] + letters[1][:j])
    palindromes = set([arr for arr in arrangements if len(arr) >= 3 and arr == arr[::-1]])
    return palindromes