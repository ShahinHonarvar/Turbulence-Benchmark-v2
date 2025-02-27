def palindromes_of_specific_lengths(s):
    s = s[16:61].lower()
    lengths = set()
    for i in range(16, 40):
        for j in range(i + 1, 40):
            subs = s[j - i:j + 1]
            if subs == subs[::-1] and subs.isalpha():
                lengths.add(subs)
    return lengths