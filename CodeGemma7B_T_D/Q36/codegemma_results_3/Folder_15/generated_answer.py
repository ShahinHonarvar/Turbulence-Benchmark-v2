def filter_chars(text):
    answer = ''
    for i in range(len(text)):
        if i not in range(2, 7):
            answer += text[i]
    return answer