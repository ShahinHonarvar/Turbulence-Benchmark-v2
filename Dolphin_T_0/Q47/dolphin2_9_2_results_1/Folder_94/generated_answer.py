def palindromes_of_specific_lengths(s):
    s = s[40:95]
    lengths = [length for length in range(45, 52) if any((s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha() for i in range(len(s) - length + 1)))]
    return set() if not lengths else {s[i:i + length] for length in lengths for i in range(len(s) - length + 1)}