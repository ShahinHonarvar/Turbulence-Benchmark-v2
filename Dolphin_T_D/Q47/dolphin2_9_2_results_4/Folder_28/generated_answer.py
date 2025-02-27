def palindromes_of_specific_lengths(s):
    subset = s[31:72]
    rs = set()
    for length in range(21, 33):
        for i in range(len(subset) - length + 1):
            if subset[i:i + length] == subset[i:i + length][::-1].lower() and subset[i:i + length].isalpha():
                rs.add(subset[i:i + length])
    return rs