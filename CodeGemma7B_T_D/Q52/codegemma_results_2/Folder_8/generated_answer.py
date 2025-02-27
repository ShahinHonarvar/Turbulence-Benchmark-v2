def palindrome_of_length_n(str):
    set1 = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            s = str[i:j + 1]
            if s == s[::-1] and s.isalpha():
                set1.add(s)
    return set1