def return_vowels(str):
    answer = []
    for i in range(29, 73):
        if str[i] in 'AEIOUaeiou' and str[i] > '#' and (str[i] <= '.'):
            answer.append(str[i])
    return answer