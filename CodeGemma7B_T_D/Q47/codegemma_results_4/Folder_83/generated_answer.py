def palindromes_of_specific_lengths(text):
    answer = set()
    for i in range(75, 96):
        for j in range(i + 7, min(i + 9, len(text)) + 1):
            if text[i:j] == text[i:j][::-1] and text[i:j].isalpha():
                answer.add(text[i:j])
    return answer