def palindromes_of_specific_lengths(s):
    substring = s[11:56]
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            sub = ''.join((ch for ch in sub if ch.isalpha()))
            sub = sub.lower()
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes