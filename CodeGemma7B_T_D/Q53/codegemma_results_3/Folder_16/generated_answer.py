def palindrome_of_length_at_least_n(str1):
    str1 = str1.lower()
    list_str = list(str1)
    answer_set = set()
    for i in range(len(str1)):
        for end in range(i + 119, len(str1) + 1):
            temp_str = ''.join(list_str[i:end])[::-1]
            if temp_str in str1:
                answer_set.add(temp_str)
    return answer_set