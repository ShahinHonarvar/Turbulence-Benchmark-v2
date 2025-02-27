def palindromes_of_specific_lengths(s):
    s = s[15:61].lower()
    lengths = range(16, 40)
    return {s[i:i + l] for l in lengths if s[i:i + l] == s[i:i + l][::-1]}