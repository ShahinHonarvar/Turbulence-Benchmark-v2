def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 445 + 1):
        if s[i:i + 445].lower() == reversed(s[i:i + 445]).lower():
            result.add(s[i:i + 445])
    return result