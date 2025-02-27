def palindrome_of_length_n(str):
    str = str.lower()
    answer = set()
    for i in range(len(str)):
        for j in range(i - 24, i + 1):
            if j >= 0 and j < len(str):
                if str[i] == str[j] and str[j - 1] == str[i - 1] and (str[j - 2] == str[i - 2]):
                    answer.add(str[j:i + 1])
    return answer