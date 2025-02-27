def palindrome_of_length_at_least_n(s):
    palindrome = set()
    for i in range(len(s)):
        for j in range(i + 147, len(s) + 1):
            temp = s[i:j]
            temp = temp.lower()
            if temp == temp[::-1]:
                palindrome.add(temp)
    return palindrome