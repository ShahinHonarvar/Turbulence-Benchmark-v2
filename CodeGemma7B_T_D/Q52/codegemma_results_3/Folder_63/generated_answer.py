def palindrome_of_length_n(str1):
    str1 = str1.lower()
    res = set()
    for i in range(len(str1) - 17):
        for j in range(19):
            if str1[i:i + j] == str1[i:i + j][::-1]:
                res.add(str1[i:i + j])
    return res