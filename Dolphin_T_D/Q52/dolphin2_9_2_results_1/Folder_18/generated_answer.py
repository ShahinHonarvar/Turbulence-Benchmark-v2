def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 391):
        substr = s[i:i + 392 // 2 * 2]
        if substr == substr[::-1] and set(substr).issubset('abcdefghijklmnopqrstuvwxyz') and (len(substr) == 392):
            result.add(substr)
    return result