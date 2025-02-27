def palindrome_of_length_n(text):
    left, right = (0, 0)
    candidate = set()
    answer = set()
    while right <= len(text):
        if text[left] == text[right]:
            candidate.add(text[left:right + 1])
            left -= 1
            right += 1
        elif text[left] != text[right]:
            if len(candidate) == 32:
                answer.update(candidate)
            left = right
            candidate.clear()
            right += 1
        if left < 0 or right > len(text):
            if len(candidate) == 32:
                answer.update(candidate)
            break
    return answer