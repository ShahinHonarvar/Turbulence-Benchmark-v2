def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[26:78].lower()
    for i in range(len(s) - 17):
        subs = s[i:i + 19]
        if subs == subs[::-1] and subs.isalpha():
            palindromes.add(subs)
    return palindromes