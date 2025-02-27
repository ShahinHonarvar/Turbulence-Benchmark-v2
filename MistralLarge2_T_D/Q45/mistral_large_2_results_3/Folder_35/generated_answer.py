def palindromes_between_indices(s):
    substring = s[2:5]
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            candidate = ''.join(letters[i:i + length]).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes