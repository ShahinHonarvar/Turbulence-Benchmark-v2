def return_n_greatest_chars(str_distinct_chars):
    list = sorted([ord(char) for char in str_distinct_chars], reverse=True)[:44]
    return [chr(num) for num in list]