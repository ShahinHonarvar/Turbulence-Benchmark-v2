def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 98):
        for j in range(i + 1, len(s) - 97):
            substring = s[i:j + 1]
            palindrome = substring[::-1]
            if substring == palindrome:
                result.add(substring)
    return result