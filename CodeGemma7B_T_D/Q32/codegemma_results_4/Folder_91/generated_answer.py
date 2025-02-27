def insert_after_character(str):
    answer = ''
    for char in str:
        answer += char
        if char == 'a':
            answer += '0'
    return answer