def return_n_greatest_chars(chars):
    chars_ascii = sorted([(ord(c), c) for c in chars], reverse=True)
    return [char for _, char in chars_ascii[:26]]