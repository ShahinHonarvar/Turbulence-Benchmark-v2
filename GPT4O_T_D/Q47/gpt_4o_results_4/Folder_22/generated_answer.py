def palindromes_of_specific_lengths(s):
    s = s[100:201]
    palindromes = set()
    n = len(s)
    for i in range(n):
        for length in range(5, 11):
            if i + length > n:
                break
            substr = s[i:i + length]
            filtered = ''.join((c.lower() for c in substr if c.isalpha()))
            if filtered == filtered[::-1] and len(filtered) == length:
                palindromes.add(filtered)
    return palindromes