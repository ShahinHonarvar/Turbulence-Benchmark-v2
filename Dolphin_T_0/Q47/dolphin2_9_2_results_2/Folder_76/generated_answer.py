def palindromes_of_specific_lengths(s):
    s = s[101:293]
    out = set()
    for length in range(154, 183):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                if substring.isalpha():
                    out.add(substring)
    return out