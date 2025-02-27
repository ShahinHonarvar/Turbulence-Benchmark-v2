def palindromes_of_specific_lengths(s):
    s = s[16:95]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.lower() == subs[::-1].lower():
                palindromes.add(subs)
    return palindromes