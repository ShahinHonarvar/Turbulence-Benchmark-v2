def palindrome_of_length_at_least_n(s):
    palindrome = set()
    for i in range(len(s)):
        for j in range(i + 7, len(s) + 1):
            temp = s[i:j]
            if temp == temp[::-1] and temp.isalpha():
                palindrome.add(temp)
    return palindrome