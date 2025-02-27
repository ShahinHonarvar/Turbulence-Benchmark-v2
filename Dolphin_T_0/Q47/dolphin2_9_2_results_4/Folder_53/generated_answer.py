def palindromes_of_specific_lengths(s):
    s = s[1:300].lower()
    result = set()
    for size in range(3, 11):
        for i in range(len(s) - size + 1):
            if s[i:i + size] == s[i:i + size][::-1] and s[i:i + size].isalpha():
                result.add(s[i:i + size])
    return result