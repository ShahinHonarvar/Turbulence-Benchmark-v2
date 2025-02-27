def palindrome_of_length_n(str):
    set()
    for i in range(len(str)):
        for j in range(i + 2, len(str)):
            if str[i] + str[j] == (str[i] + str[j])[::-1]:
                set.add(str[i] + str[j])
    return set