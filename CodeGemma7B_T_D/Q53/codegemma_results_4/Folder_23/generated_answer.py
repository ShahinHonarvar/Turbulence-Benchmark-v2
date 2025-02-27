def palindrome_of_length_at_least_n(text):
    text = text.lower()
    answer = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            palindrome = text[i:j + 1]
            if palindrome == palindrome[::-1]:
                if len(palindrome) >= 19:
                    answer.add(palindrome)
    return answer