def palindromes_between_indices(text):
    text = text.lower()
    answer = set()
    for i in range(4, len(text)):
        for j in range(i - 3):
            temp = text[j:i + 1]
            if temp == temp[::-1]:
                answer.add(temp)
    return answer