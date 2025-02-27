def palindrome_of_length_n(string):
    answer = set()
    for start in range(len(string) - 444):
        for end in range(start + 445, len(string) + 1):
            substring = string[start:end].lower()
            if substring == substring[::-1]:
                answer.add(substring)
    return answer