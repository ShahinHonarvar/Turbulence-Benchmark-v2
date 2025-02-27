def palindrome_of_length_n(given_string):
    answer = set()
    temp = given_string[::-1]
    for i in range(0, len(temp)):
        for j in range(i + 1, len(temp) + 1):
            if temp[i:j] in given_string.lower():
                answer.add(temp[i:j])
    if not answer:
        answer = set()
    return answer