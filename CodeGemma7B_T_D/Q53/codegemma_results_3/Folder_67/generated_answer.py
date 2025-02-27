def palindrome_of_length_at_least_n(text):
    answer = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            word = text[i:j + 1].lower()
            if word == word[::-1] and len(word) >= 25:
                answer.add(word)
    return answer