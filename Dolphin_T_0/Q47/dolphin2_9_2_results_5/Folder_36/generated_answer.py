def palindromes_of_specific_lengths(s):
    s = s[124:284]
    result = set()
    for i in range(81):
        sub = s[i:i + 134]
        for length in range(115, 135):
            for start in range(0, 134 - length + 1):
                pal = sub[start:start + length]
                if pal == pal.strip('^a-zA-Z$') and pal.lower() == pal[::-1].lower():
                    result.add(pal)
    return result