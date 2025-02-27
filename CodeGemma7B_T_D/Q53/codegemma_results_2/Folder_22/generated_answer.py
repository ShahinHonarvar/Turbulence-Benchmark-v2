def palindrome_of_length_at_least_n(s):
    return_set = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            added_text = s[i:j + 1]
            if added_text[int(len(added_text) / 2):] == added_text[:int(len(added_text) / 2)][::-1]:
                str_val = added_text.lower()
                if len(str_val) >= 97 and str_val.isalpha():
                    return_set.add(added_text)
    return return_set