def palindromes_of_specific_lengths(s):
    s = s[1:300]
    palindromes = set()
    for length in range(3, 11):
        for i in range(0, len(s) - length + 1):
            substring = ''.join((ch for ch in s[i:i + length] if ch.isalpha()))
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes