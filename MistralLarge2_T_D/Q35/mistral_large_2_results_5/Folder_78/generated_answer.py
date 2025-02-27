def remove_repeat_chars(s):
    relevant_section = s[62:96]
    to_remove = {char for char in relevant_section if relevant_section.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))