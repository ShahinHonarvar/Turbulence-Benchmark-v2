import re

def remove_repeat_chars(s):
    return re.sub('([^aieouAEIOU]){200,202}(.)([^aieouAEIOU]){200,202}', '\x01\x02', s)