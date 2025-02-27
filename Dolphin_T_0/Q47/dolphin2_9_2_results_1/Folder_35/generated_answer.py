def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(14, 40):
        for i in range(34, 91):
            subs = s[i:i + length]
            subs_low = subs.lower()
            if all(('a' <= letter <= 'z' for letter in subs_low)) and subs_low == subs_low[::-1]:
                palindromes.add(subs)
    return palindromes