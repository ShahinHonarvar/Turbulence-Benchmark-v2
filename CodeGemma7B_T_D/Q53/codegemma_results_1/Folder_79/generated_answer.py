def palindrome_of_length_at_least_n(text):
    text = text.lower()
    answer = set()
    for i in range(len(text)):
        for j in range(i + 17, len(text) + 1):
            temp = text[i:j]
            if temp == temp[::-1]:
                answer.add(temp)
    return answer