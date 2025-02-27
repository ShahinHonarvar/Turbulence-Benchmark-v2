def palindrome_of_length_at_least_n(s):
    English_letters_lowercase = set('abcdefghijklmnopqrstuvwxyz')
    English_letters_uppercase = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = ''.join((e for e in s if e in English_letters_lowercase or e in English_letters_uppercase))
    result_set = set()
    for i in range(len(s)):
        for j in range(i + 137, len(s) + 1):
            sub_string = s[i:j]
            sub_string_lowercase = sub_string.lower()
            sub_string_uppercase = sub_string.upper()
            if sub_string_lowercase == sub_string_lowercase[::-1] and sub_string_uppercase == sub_string_uppercase[::-1]:
                result_set.add(sub_string)
    return result_set