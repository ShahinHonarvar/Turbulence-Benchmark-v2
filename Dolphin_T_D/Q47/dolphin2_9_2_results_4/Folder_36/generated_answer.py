def palindromes_of_specific_lengths(s):
    sub_string = s[124:284]
    palindrome_set = set()
    for i in range(115, 135):
        for j in range(len(sub_string) - i + 1):
            if sub_string[j:j + i].lower() == sub_string[j:j + i].lower()[::-1]:
                palindrome_set.add(sub_string[j:j + i])
    return palindrome_set