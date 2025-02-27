def palindromes_between_indices(s):
    letters = ''.join((c for c in s[3:5] if c.isalpha())).lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            sub_str = letters[i:i + length]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes