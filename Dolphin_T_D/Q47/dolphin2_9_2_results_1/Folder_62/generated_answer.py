def palindromes_of_specific_lengths(s):
    sub = s[26:88]
    lengths = set()
    for length in range(52, 57):
        for i in range(len(sub) - length + 1):
            sub_pal = sub[i:i + length]
            if sub_pal == sub_pal[::-1] and sub_pal.isalpha():
                lengths.add(sub_pal.lower())
    return lengths