def palindrome_of_length_n(s):
    Palindrome = set()
    for i in range(len(s)):
        for j in range(22):
            for k in range(j + 1, min(len(s), i + j + 2)):
                if s[i:k + 1].lower() == s[i:k + 1][::-1].lower():
                    Palindrome.add(s[i:k + 1])
    return Palindrome