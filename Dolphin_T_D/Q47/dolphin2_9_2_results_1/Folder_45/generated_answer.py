def palindromes_of_specific_lengths(s):
    en_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s[70:141]
    palindromes = set()
    for length in range(3, 61):
        for start in range(0, len(s) - length + 1):
            substr = s[start:start + length].lower()
            if all((c in en_letters for c in substr)) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes