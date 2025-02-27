def palindrome_of_length_n(str):
    pali = set()
    str = str.lower()
    for i in range(len(str) - 66):
        temp = str[i:i + 67]
        if temp == temp[::-1]:
            pali.add(temp)
    return pali