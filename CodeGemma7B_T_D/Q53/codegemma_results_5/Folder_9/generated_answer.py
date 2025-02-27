def palindrome_of_length_at_least_n(string):
    length_of_string = len(string)
    answer = set()
    for i in range(length_of_string):
        for j in range(i, min((i + 48, length_of_string))):
            substring = string[i:j + 1]
            if substring == substring[-1::-1] and len(substring) >= 95:
                answer.add(substring.lower())
    return answer