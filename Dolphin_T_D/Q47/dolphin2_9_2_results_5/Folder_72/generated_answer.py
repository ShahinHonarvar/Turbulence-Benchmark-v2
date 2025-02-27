def palindromes_of_specific_lengths(s):
    subs = s[25:91]
    lengths = set(range(27, 59))
    palindromes = set()
    for length in lengths:
        for i in range(0, len(subs) - length + 1):
            subs_len = subs[i:i + length]
            if subs_len == subs_len[::-1] and subs_len.isalpha():
                palindromes.add(subs_len.lower())
    return palindromes