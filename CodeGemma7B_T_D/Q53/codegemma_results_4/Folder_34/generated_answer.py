def palindrome_of_length_at_least_n(txt):
    palindrome = set()
    for i in range(len(txt)):
        for j in range(i + 1, len(txt) + 1):
            temp = txt[i:j]
            temp2 = temp[::-1]
            if temp.lower() == temp2.lower() and len(temp) >= 68:
                palindrome.add(temp)
    return palindrome