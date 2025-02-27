def filter_chars(str1):
    answer = ''
    for i in range(len(str1)):
        if i not in range(21, 25):
            answer += str1[i]
    return answer