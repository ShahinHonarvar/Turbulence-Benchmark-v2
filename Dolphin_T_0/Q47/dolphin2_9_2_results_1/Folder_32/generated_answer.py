def palindromes_of_specific_lengths(s):
    s = s[15:78]
    lengths = range(43, 48)
    palindromes = set()
    for length in lengths:
        for i in range(len(s)):
            sub_s = s[i:i + length]
            if sub_s == sub_s.lower() and sub_s[::-1].lower() == sub_s.lower():
                for char in sub_s:
                    if not char.isalpha():
                        break
                else:
                    palindromes.add(sub_s)
    return palindromes