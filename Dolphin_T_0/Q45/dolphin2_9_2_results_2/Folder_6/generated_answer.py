def palindromes_between_indices(s):
    letters = [ch for ch in s if ch.isalpha()]
    length = len(letters)
    if length < 4:
        return set()
    palindromes = set()
    for i in range(length):
        for j in range(i + 3, length):
            substring = ''.join(letters[i:j + 1])
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes